Name: gnetdict
Version: 0.2.5.1
Release: 1
Summary: GTK+ Net Dictionary
Summary(zh_TW): GTK+ 網路辭典
License: GPL
Group: Applications/Internet
Source: https://rt.openfoundry.org/Foundry/Project/Download/Attachment/92913/63831/gnetdict-0.2.5.1.tar.bz2
Vendor: Hong Jen Yee (PCMan)   <pcman.tw( at )gmail.com>
Requires: python, pygtk2, gnome-python2-gtkhtml2
BuildArch: noarch

%description
A GTK+ front-end of various online free dictionaries
for searching words conveniently and quickly.

%description -l zh_TW
各種線上免費辭典的 GTK+ 前端介面，
查單字方便又快速。

%prep
%setup -q
%{__sed} -i 's|~/.gnetdict/|/usr/lib/gnetdict/|' gnetdict.py
%{__sed} -i 's|/usr/lib/gnetdict/config|~/.gnetdict/config|' gnetdict.py
%{__sed} -i '/#global variables/a if not os.path.exists(os.path.expanduser("~/.gnetdict/")):\n    os.mkdir(os.path.expanduser("~/.gnetdict/"))\nif not os.path.exists(os.path.expanduser("~/.gnetdict/config")):\n    f=open(os.path.expanduser("~/.gnetdict/config"),"w")\n    f.close()' gnetdict.py

%build
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install
%__install -D -m 755 scripts/edudict.py %{buildroot}%{_libdir}/%{name}/scripts/edudict.py
%__install -D -m 755 scripts/yahoo.py %{buildroot}%{_libdir}/%{name}/scripts/yahoo.py

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_libdir}/%{name}/scripts/*.py %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING README
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Mar 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.5.1
- Rebuilt for Fedora
