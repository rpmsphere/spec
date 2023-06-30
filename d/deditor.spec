Name: deditor
Summary: Text-Editor for python users
Version: 0.4.0
Release: 1
Group: python
License: Free Software
URL: https://launchpad.net/deditor/
Source0: %{name}_%{version}_all.deb
#Source0: %{name}.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: python2-devel

%description
Deditor is a text-editor written in python using the wxpython toolkit.
It is made for python users, autocompletion, direct shell access,...
Other programming languages are also supported

%prep
%setup -T -c

%build
ar -x %{SOURCE0}

%install
mkdir -p %{buildroot}
tar xf data.tar.gz -C %{buildroot}
sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}.py %{buildroot}%{_datadir}/%{name}/dplug/main.py
#install -d %{buildroot}%{_bindir}
#ln -s ../share/%{name}/%{name}.py %{buildroot}%{_bindir}/%{name}
#install -d %{buildroot}%{_datadir}/%{name}
#cp -a config data %{name}.py dplug plugins %{buildroot}%{_datadir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/deditor.desktop
%{_datadir}/doc/deditor
%{_datadir}/pixmaps/deditor.gif
%{_datadir}/python-support/deditor.private

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
