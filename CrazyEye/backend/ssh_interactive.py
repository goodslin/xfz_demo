from django.contrib.auth import authenticate


class SshHandler(object):
    """启动堡垒机交互脚本"""

    def __init__(self, argv_handler_instance):
        self.argv_handler_instance = argv_handler_instance

    def auth(self):
        """认证程序"""
        count = 0
        while count < 3:
            username = input("堡垒机账号：").strip()
            password = input("密码：").strip()
            user = authenticate(username=username, password=password)
            if user:
                self.user = user
                return True
            else:
                count += 1

    def interactive(self):
        """启动交互脚本"""
        if self.auth():
            print("Ready to print all the authorized host...to this user...")
            while True:
                host_group_list = self.user.host_groups.all()
                for index, host_group_obj in enumerate(host_group_list):
                    print("%s.\t%s[%s]" % (index, host_group_obj.name, host_group_obj.host_to_remote_users.count()))

                choice = input("请选择主机组>>:")
                if choice.isdigit():
                    choice = int(choice)
                    selected_host_group = host_group_list[choice]
                elif choice == 'z':
                    selected_host_group = self.user

                while True:
                    for index, host_to_user_obj in enumerate(selected_host_group.host_to_remote_users.all()):
                        print("%s.\t%s" % (index, host_to_user_obj))

                    choice = input("请选择主机>>:").strip()
                    if choice.isdigit():
                        choice = int(choice)
                        selected_host_to_user_obj = selected_host_group.host_to_remote_users.all()[choice]
                        print("going to logon %s" % selected_host_to_user_obj)
                    if choice == 'b':
                        break
