%undefine _debugsource_packages
Name:		lookit
Version:	0.4.0
Release:	1
Summary:	A Quick Screenshot Uploader
License:	GPLv2
Group:		Applications/Multimedia
URL:		https://launchpad.net/~lookit
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	pygtk2, python-appindicator, python-keyring, python-keybinder

%description
Take and upload screenshots quickly with Lookit. Lookit allows you to quickly
capture all or part of your screen and automatically uploads it to the SFTP
or FTP server of your choice. Then, an (optionally shortened) URL is placed
on your clipboard, ready for easy sharing.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --prefix=%{_prefix} --root %{buildroot}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{python2_sitelib}/%{name}-%{version}-py*.egg-info
%{python2_sitelib}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*.svg

%changelog
* Mon Mar 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
