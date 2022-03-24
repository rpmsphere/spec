Name: easyshutdown
Summary: An easy script to shutdown your computer.
Version: 0.6
Release: 1
Group: doc
License: Free Software
Source0: easyshutdown_0.6_all.deb
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: python2-devel

%description
You can specify hours and minutes after which your computer will turn off.

%prep
%setup -T -c

%build
ar -x %{SOURCE0}

%install
mkdir -p %{buildroot}
tar xf data.tar.gz -C %{buildroot}

%files
%{_bindir}/%{name}.py
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{name}/
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.2
- Rebuilt for Fedora
