from . import logger_func

def check_access(*args, user_roleId=False, user=None):
	if user_roleId:
		status = check_access_on_id(args, user_roleId)
		return status
	if user:
		status = check_access_on_user(args, user)
		return status

def check_access_on_id(access_id, user_roleId):
	for role_id in access_id:
		if role_id == user_roleId:
			return True
	return False
	
def check_access_on_user(access_user, user):
	for userList in access_user:
		for userInList in userList:
			if userInList == user:
				return True
	return False


if __name__ == "__main__":
	print(check_access(1,2,3, user_roleId=5))
	print(check_access(1,2,3, user_roleId=1)) 