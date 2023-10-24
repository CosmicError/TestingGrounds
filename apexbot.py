teams = {
    [1234654] : {
        ["Main"]: [1234654, 56789, 65798], 
        ["School"]: "KSU"
        }
    }

priority = {
    ["KSU"] : {
        ["Black"] : [
            1, 
            2,
            [1234654, 56789, 568745]
        ]
    }
}

queue = []
lobby = {
    [1] : [[1234654],]
}

#? NORAML
# !register [school] [players]
# !add [school] [team]
# !drop

#? ADMIN
# !remove [school] [team]
# !fadd [school] [team]
# !fdrop [captin]
# !roll 
    #?(gives lobby 1, 2 or 3 role)
# !op [admin]
# !deop [admin]
