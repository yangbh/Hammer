var json = {
  "global": {
    "target": "http://testphp.vulnweb.com",
    "loglevel": "INFO",
    "threads": 4,
    "mode": "1",
    "timeout": 10,
    "gatherdepth": 1
  },
  "plugins": {
    "Weak_Password": {
      "run": true
    },
    "Sensitive_Info": {
      "run": true
    },
    "Info_Collect": {
      "subdomain": true,
      "crawler": {
        "useragent": "",
        "cookies": "",
        "exlude": "",
        "isexlude": "0"
      },
      "portscan": {
        "timeout": 20,
        "arguments": "just a test"
      },
      "run": "1",
      "isneiborhost": true
    },
    "System": {
      "run": true
    },
    "Common": {
      "run": true
    },
    "Others": {
      "run": true
    },
    "Web_Applications": {
      "run": true
    }
  }
};



