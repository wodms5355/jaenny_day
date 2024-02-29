

class Member:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):

        print("이름:", self.name, "ID:", self.username)
        result = self.name + self.username
        return result



member1 = Member("재은", "jaenny_day", "1234")
member2 = Member("지윤", "09.03._.98", "4567")
member3 = Member("종은", "is_._u", "7890")
input("시작하나요?")
    
name = input("이름을 입력하세요:")
username = input("ID를 입력하세요:")
password = input("비밀번호를 입력하세요:")


new_member = Member(name, username, password)
print("새로운 회원이 생성됐습니다")
print(f"이름:{new_member.name}",f"ID{new_member.username}",f"비밀번호: {new_member.password}")




# if input(f"{member1.name}") == f"{member1.name}":
#    print(member1)
# elif f"{member2.name}" == f"{member2.name}":
#    print(member2)
# elif f"{member3.name}" == f"{member3.name}":
#    print(member3)
'''
    # member1.display()
    # member2.display()
    # member3.display()
'''


class Post:

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

        print("제목:", self.title, ",", "주제:",self.content, ",", "출처:", self.author)

    def posting(self):
        print("제목:", self.title, "주제:", self.content, "출처:", self.author)
        print(f"{self.title}""(이)"f"라는 주제로 {self.content}을""(를)""소개해보겠습니다.")
        print(f"출처 :{self.author}")

title = input("원하는 게시물의 제목을 입력하세요:")
content = input("원하는 게시물의 주제를 입력하세요:")
author = input("해당 게시물의 출처를 입력해주세요:")
new_post = Post(title,content,author)
print("새로운 게시글이 등록되었습니다")
print(f"제목:{new_post.title}" , f"주제:{new_post.content}" , f"출처:{new_post.author}")

post1 = Post(f"해외여행", "먹방", member1.username)
post2 = Post(f"헬짱", "덤벨사용법", member2.username)
post3 = Post(f"승무원", "비행안전수칙", member3.username)
post4 = Post(f"다이어트", "단백질간식", member1.username)
post5 = Post(f"제주살이", "제주감성카페", member2.username)
post6 = Post(f"워킹홀리데이", "호주워홀", member3.username)
post7 = Post(f"여수", "현지인맛집", member1.username)
post8 = Post(f"분당", "성남과는 다른곳", member2.username)
post9 = Post(f"원주", "감자사용설명서", member3.username)



#
'''
    # post1.posting()
    # post2.posting()
    # post3.posting()
    # post4.posting()
    # post5.posting()
    # post6.posting()
    # post7.posting()
    # post8.posting()
    # post9.posting()
'''

members = [member1, member2, member3,new_member]
posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9,new_post]
#members.append(new_member) 
#posts.append(new_post)



for member in members:
    member.display()

for post in posts:
    post.posting()

for member in members:
    if member.name == f"{member1.name}":
        print(f"{member1.name}이가 작성한 게시물의 제목은:")
        print(post1.title, post4.title, post7.title)
    elif member.name == f"{member2.name}":
        print(f"{member2.name}이가 작성한 게시물의 제목은:")
        print(post2.title, post5.title, post8.title)
    elif member.name == f"{member3.name}":
        print(f"{member3.name}이가 작성한 게시물의 제목은:")
        print(post3.title, post6.title, post9.title)


keywords = [{post7.content}, {post8.content}, {post9.content}]
for keyword in keywords:
    if keyword == {post7.content}:
        print(f"{post7.content}을 주제로한 게시물의 제목은?")
        print(post7.title)
    elif keyword == {post8.content}:
        print(f"{post8.content}을 주제로한 게시물의 제목은?")
        print(post8.title)
    elif keyword == {post9.content}:
        print(f"{post9.content}를 주제로한 게시물의 제목은?")
        print(post9.title)


'''
    # members.append(member1)
    # members.append(member2)
    # members.append(member3)


    # posts.append(post1)
    # posts.append(post2)
    # posts.append(post3)
    # posts.append(post4)
    # posts.append(post5)
    # posts.append(post6)
    # posts.append(post7)
    # posts.append(post8)
    # posts.append(post9)
'''
