Name:		gmountiso
Version:	0.4
Release:	1
Summary:	A tool for mounting iso9660 files.
Summary(zh_TW):	光碟映像檔的掛載工具
License:	GPL
Group:		Applications/System
Source0:	%{name}_%{version}-0ubuntu2.tar.gz
Source1:	%{name}-%{version}.zh_TW.po
BuildArch:	noarch
Requires:	pygtk2, gksu

%description
Using PyGTK2 to perform a menu-driven mounter
for managing iso9660 files.

%description -l zh_TW
利用 PyGTK2 來實作的選單驅動掛載程式，
以管理光碟映像檔案。

%prep
%setup -q
%__mv locale/zh locale/zh_CN
%__mkdir -p locale/zh_TW/LC_MESSAGES
%__cp %{SOURCE1} locale/zh_TW/LC_MESSAGES/Gmount-iso.po

%build
msgfmt locale/zh_TW/LC_MESSAGES/Gmount-iso.po -o locale/zh_TW/LC_MESSAGES/Gmount-iso.mo
echo -e 'Name[zh_TW]=映像檔掛載工具\nComment[zh_TW]=以 Gmountiso 掛載光碟映像檔' >> gmount-iso.desktop
%__sed -i 's|/usr/bin/env|/bin/env|' Gmount-iso.py
%__sed -i "s|'/home/' + commands.getoutput('whoami')|os.environ['HOME']|" Gmount-iso.py

%install
%__rm -rf %{buildroot}
%__install -D -m 755 Gmount-iso.py %{buildroot}%{_datadir}/%{name}/Gmount-iso.py
%__mkdir %{buildroot}%{_bindir}
ln -s ../share/%{name}/Gmount-iso.py %{buildroot}%{_bindir}/Gmount-iso
%__install -D -m 644 gmount-iso.glade %{buildroot}%{_datadir}/%{name}/gmount-iso.glade
%__install -D -m 644 gmount-iso.desktop %{buildroot}%{_datadir}/applications/gmount.desktop
%__install -D -m 644 Ico_gmount.png %{buildroot}%{_datadir}/pixmaps/Ico_gmount.png
%__cp -a locale %{buildroot}%{_datadir}
%__rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/Gmount-iso.po

sed -i 's|/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%clean
%__rm -rf %{buildroot}

%files
%doc GPL
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/locale/*/LC_MESSAGES/*.mo

%changelog
* Fri Mar 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
