%global debug_package %{nil}

Name:		doublecmd
Summary:	Twin-panel (commander-style) file manager
Version:	0.9.9
Release:	1
URL:		http://doublecmd.sourceforge.net
Source0:	http://sourceforge.net/projects/doublecmd/files/Double%20Commander%20Source/%{name}-%{version}-src.tar.gz
License:	GPL
Group:		File tools
BuildRequires:	fpc
BuildRequires:	fpc-src
BuildRequires:	glib2-devel
BuildRequires:	lazarus
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(dbus-1) 
BuildRequires:  bzip2-devel

%description
Double Commander is a cross platform open source file manager with two panels
side by side. It is inspired by Total Commander and features some new ideas.

%prep
%setup -q
#sed -i 's|TabIndexAtClientPos|IndexOfPageAt|' src/*.pas

%build
./build.sh beta gtk2

%install
install/linux/install.sh --install-prefix=%{buildroot}
%ifarch aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/man/man1/%{name}.*
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/polkit-1/actions/org.%{name}.root.policy

%changelog
* Wed Aug 26 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.9
- Rebuilt for Fedora
* Thu Jul 5 2012 - Konstantin Vlasov <konstantin.vlasov@rosalab.ru>
- New package from developer's site, version 0.5.4
