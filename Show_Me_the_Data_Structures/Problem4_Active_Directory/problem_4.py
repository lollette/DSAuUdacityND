
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def tree_traversal(group, visited, user):
    if user in group.users:
        return True

    for gr in group.groups:
        if gr.get_name() not in visited:
            visited[gr.get_name()] = group.get_name()
            if tree_traversal(gr, visited, user):
                return True
    return False


parent = Group("parent")
group = Group("group")
sub_group = Group("subgroup")

sub_group_user = "sub_group_user"
sub_group.add_user(sub_group_user)

group.add_group(sub_group)
parent.add_group(group)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to greck user membership against
    """
    visited = {group.get_name(): None}
    return tree_traversal(group, visited, user)


def printing_fct(user, group):
    print(user + " is in " + group.get_name() if is_user_in_group(user, group)
          else user + " is not in " + group.get_name())


printing_fct("sub_group_user", sub_group)
printing_fct("sub_group_user", group)
printing_fct("sub_group_user", parent)
printing_fct("other_user", parent)


# My tests

parent = Group("parent")

group_1 = Group("group1")
group_2 = Group("group2")

sub_group_1 = Group("subgroup1")
sub_group_2 = Group("subgroup2")
sub_group_3 = Group("subgroup3")

paren_user = "parent_user"
parent.add_user(paren_user)
parent.add_group(group_1)
parent.add_group(group_2)

group_1_user = "group_1_user"
group_1.add_user(group_1_user)
group_1.add_group(sub_group_1)

group_2.add_group(sub_group_2)
group_2.add_group(sub_group_3)

sub_group_3_user_1 = "sub_group_3_user_1"
sub_group_3.add_user(sub_group_3_user_1)
sub_group_3_user_2 = "sub_group_3_user_2"
sub_group_3.add_user(sub_group_3_user_2)

sub_group_2.add_group(sub_group_3)
sub_group_3.add_group(sub_group_2)


# user in group
assert(is_user_in_group(paren_user, parent))
assert(is_user_in_group(group_1_user, group_1))
assert(is_user_in_group(sub_group_3_user_1, sub_group_3))
assert(is_user_in_group(sub_group_3_user_2, sub_group_3))


# user in child group
assert(is_user_in_group(group_1_user, parent))
assert(is_user_in_group(sub_group_3_user_1, group_2))
assert(is_user_in_group(sub_group_3_user_2, group_2))


# user in sub-child group
assert(is_user_in_group(sub_group_3_user_1, parent))
assert(is_user_in_group(sub_group_3_user_2, parent))

# user that does not exist
assert not (is_user_in_group("anonymous", parent))

# user wrong group from top to bottom
assert not (is_user_in_group(paren_user, sub_group_2))

# user wrong group from bottom to top
assert not (is_user_in_group(sub_group_3_user_2, group_1))

# user wrong group same level
assert not (is_user_in_group(group_1_user, sub_group_1))

# circular group
assert(is_user_in_group(sub_group_3_user_2, sub_group_2))

