%define theme_name Nerdy-Lines

Summary: %{theme_name} icon theme
Name: nerdy-lines-icon-theme
Version: 0.2.0
Release: 3.1
License: CC BY-NC-ND
URL: http://www.christophbrill.de/en_US/nerdy-lines-icons/
Group: User Interface/Desktops
Source: Nerdy-Lines-%{version}.tar.bz2
BuildArch: noarch

%description
This theme is based on the Kreski Lines icon theme. The main problem was that
the original theme was not scalable. And also incomplete. That gave my desktop
an incomplete look. So I decided to fix that. The result is that they were
redrawn from scratch in SVG-format.

%prep
%setup -q -n Nerdy-Lines

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -R * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Feb 17 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
