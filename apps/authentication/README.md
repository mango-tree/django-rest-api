# django-rest-api authentication

## Facebook Social Login

����, testapp�� ������/�׽��ͷ� ����� �Ǿ��־�� ��.

#### Environment Setting
���ÿ��� ������ �� ��, localhost.3000won.com:������Ʈ/facebook/ ���� �����ϸ� facebook �α��� ��ư�� ��.
�α��� ��, ��ū�� �α׿� ������(�ڹٽ�ũ��Ʈ FB.getAccessToken() �Լ��� ���� �� ����).
localhost.3000won.com:������Ʈ/api-auth/      <<< POST�� ������( {"auth_token": (��Ͽ��� ���� ��ū)} )
�ڵ����� ȸ������&�α����� �Ϸ�ȴ�.
