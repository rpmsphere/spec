Name:           google-appengine-python
Version:	1.6.1
Release:	36.1
License:	Apache-2
Summary:	Google App Engine SDK for Python
URL:		https://code.google.com/intl/en/appengine
Group:		Development/Tools/Other
Source:		%{name}-%{version}.tar.bz2
Source2:	setpath.sh
BuildArch:	noarch

%description
Google App Engine enables you to build and host web apps on the same systems
that power Google applications. App Engine offers fast development and
deployment; simple administration, with no need to worry about hardware,
patches or backups; and effortless scalability.

%package lang
License:	Apache-2
Summary:	Google App Engine SDK for Python
Group:		Development/Tools/Other
Requires:	%{name} = %{version}

%description lang
Google App Engine enables you to build and host web apps on the same systems
that power Google applications. App Engine offers fast development and
deployment; simple administration, with no need to worry about hardware,
patches or backups; and effortless scalability.

%package -n %{name}-yaml-devel
License:	Apache-2
Summary:	Google App Engine SDK for Python
Group:		Development/Tools/Other
Requires:	%{name} = %{version}

%description -n %{name}-yaml-devel
Google App Engine enables you to build and host web apps on the same systems
that power Google applications. App Engine offers fast development and
deployment; simple administration, with no need to worry about hardware,
patches or backups; and effortless scalability.

%prep
%setup -q

%build
#fix non-executable-script warning
find ./ -type f -name "*.py" | xargs sed -i '/^#!\/usr\/bin\/env python$/d'
find ./ -type f -name "*.py" | xargs sed -i '/^#!\/usr\/bin\/python2\.4$/d'
find ./ -type f -name "*.py" | xargs sed -i '/^#!\/usr\/bin\/python$/d'
find ./ -type f -name "*" | xargs sed -i '/^#!\/usr\/bin\/env$/d'
find ./ -type f -name "*.sh" -print -exec chmod +x {} \;
chmod +x lib/webob/test
sed -i '1d' lib/python-gflags/debian/rules
sed -i '1d' lib/google-api-python-client/bin/enable-app-engine-project 
sed -i '1d' lib/enum/enum/test/test_enum.py
#fix shebang 
sed -i '1i#!/usr/bin/env python' dev_appserver.py appcfg.py bulkload_client.py bulkloader.py gen_protorpc.py google_sql.py remote_api_shell.py 
sed -i '1i#!/usr/bin/env python' tools/bulkload_client.py
chmod -x lib/google-api-python-client/setpath.sh

#fix zero-length
find ./lib/django_1_2/tests/*/*/ -type f -name "models.py" -print -delete
find ./lib/django_1_2/django/contrib/*/ -type f -name "models.py" -print -delete
find ./lib/django_1_2/django/contrib/*/*/*/*/ -type f -name "login.html" -print -delete

%install
rm -f -r $RPM_BUILD_ROOT
%{__mkdir} -pv $RPM_BUILD_ROOT%{_bindir}
%{__mkdir} -pv $RPM_BUILD_ROOT/opt/%{name}/
%{__mkdir} -pv $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/

%{__cp} -r * $RPM_BUILD_ROOT/opt/%{name}/
%{__cp} %{S:2} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/%{name}.sh

#fix python-bytecode-inconsistent-mtime
find $RPM_BUILD_ROOT -type f -name "*.pyc" -print -delete

ln -sf /opt/%{name}/appcfg.py $RPM_BUILD_ROOT%{_bindir}

%find_lang djangojs %no_lang_C %{name} 
%find_lang django %no_lang_C %{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}/opt/google-appengine-python/*.py %{buildroot}/opt/google-appengine-python/tools/*.py

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/profile.d/%{name}.sh
/opt/%{name}/
%{_bindir}/appcfg.py
%exclude /opt/%{name}/lib/django_*_*/django/conf/locale/
%exclude /opt/%{name}/google/appengine/*/django/conf/locale/
%exclude /opt/%{name}/lib/django*/tests/*/locale/
%exclude /opt/%{name}/lib/django*/tests/*/*/locale/
%exclude /opt/%{name}/lib/django*/tests/*/*/*/locale/
%exclude /opt/%{name}/lib/yaml/ext/

%files -n %{name}-yaml-devel
/opt/%{name}/lib/yaml/ext/

%files lang -f %{name}
%dir /opt/%{name}/lib/django_*_*/django/conf/locale/
%dir /opt/%{name}/lib/django_*_*/django/conf/locale/*/
%dir /opt/%{name}/lib/django_*_*/django/conf/locale/*/*/
%dir /opt/%{name}/lib/django*/tests/*/*/*/locale/
%dir /opt/%{name}/lib/django*/tests/*/*/*/locale/*/
%dir /opt/%{name}/lib/django*/tests/*/*/*/locale/*/*/
%dir /opt/%{name}/lib/django*/tests/*/*/locale/
%dir /opt/%{name}/lib/django*/tests/*/*/locale/*/
%dir /opt/%{name}/lib/django*/tests/*/*/locale/*/*/
%dir /opt/%{name}/lib/django*/tests/*/locale
%dir /opt/%{name}/lib/django*/tests/*/locale/*/
%dir /opt/%{name}/lib/django*/tests/*/locale/*/*/
%dir /opt/%{name}/google/appengine/*/*/*/locale
%dir /opt/%{name}/google/appengine/*/*/*/locale/*/
%dir /opt/%{name}/google/appengine/*/*/*/locale/*/*/

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.1
- Rebuilt for Fedora
* Sun Dec 25 2011 i@marguerite.su
- fixed all errors and warnings, add setpath.sh to set path for
  outside directory execute.
* Fri Dec 23 2011 i@marguerite.su
- initial package 1.6.1
