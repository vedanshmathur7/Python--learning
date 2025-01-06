def http_status (status):
    match status :
        case 200 :
            print ("OK")
        case 404:
            print ("Not found")
        case 500:
            print ("Internal server error")
        case _:
            print ("Unknown status")

http_status(404)
http_status(200)
http_status(500)
http_status("_")