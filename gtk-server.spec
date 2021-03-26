%global debug_package %{nil}
%global __spec_install_post %{nil}

Summary: Interpreted GUI Programming
Name: gtk-server
Version: 2.4.3
Release: 27.1
Source0: http://www.gtk-server.org/stable/%{name}-%{version}.tar.gz
URL: http://www.gtk-server.org/
License: GPL
Group: Development/Tools
BuildRequires: libffi-devel
BuildRequires: gtk3-devel
BuildRequires: openssl-devel

%description
The GTK-server enables GUI access to script- and
interpreted languages, using the famous GTK widget
set. It can be used with Bourne Shell, Korn Shell,
GNU Awk, CLisp, newLisp, Perl, CShell and many other
languages.

%prep
%setup -q

%build
cd src
%configure
sed -i 's|BINDIR =.*|BINDIR =   %{buildroot}%{_bindir}|' Makefile
sed -i 's|LIBDIR =.*|LIBDIR =   %{buildroot}%{_libdir}|' Makefile
sed -i 's|SYSCONFIG =.*|SYSCONFIG =   %{buildroot}%{_sysconfdir}|' Makefile
sed -i 's|MANDIR =.*|MANDIR =   %{buildroot}%{_mandir}|' Makefile
sed -i '/ln -sf/d' Makefile
sed -i 's|-Wall|-Wall -fPIC|' Makefile
make

%install
cd src
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CREDITS README.1ST documentation/*
%config /etc/gtk-server.cfg
%{_bindir}/*
%{_libdir}/lib*.so
%{_mandir}/man1/*

%changelog
* Mon Aug 21 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.3
- Rebuild for Fedora
* Thu Feb 26 2009 Peter van Eerten <peter AT gtk-server DOT org>
- Initial package
