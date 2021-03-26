%global debug_package %{nil}

Summary: Lars Tiling Window Manager
Name: larswm
Version: 7.5.3
Release: 8.1
License: GPL
Group: User Interface/Desktops
Source: http://sourceforge.net/projects/larswm/files/%{name}-%{version}.tar.gz
URL: http://sourceforge.net/projects/larswm/
BuildRequires: imake libX11-devel libXext-devel libXmu-devel

%description
This is a small tiling window manager based on David Hogan's 9wm.

%prep
%setup -q

%build
xmkmf -a
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 0755 larswm $RPM_BUILD_ROOT%{_bindir}/larswm
install -Dm 0644 larswm.man $RPM_BUILD_ROOT%{_mandir}/man1/larswm.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog README sample.larswmrc README.9wm
%{_bindir}/larswm
%{_mandir}/man1/larswm.1.*

%changelog
* Mon Jan 20 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 7.5.3
- Rebuild for Fedora
