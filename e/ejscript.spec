%global __os_install_post %{nil}
%undefine _debugsource_packages

Summary: The smallest, embeddable implementation of Javascript ES6
Name: ejscript
Version: 2.7.7
Release: 1
License: commercial, GPL
Group: Development/Languages
#Source0: https://s3.amazonaws.com/embedthis.public/%{name}-%{version}.tar.gz
Source0: %{name}-master.zip
URL: https://www.embedthis.com/ejscript/

%description
Ejscript is a complete, integrated JavaScript environment suitable for
education purposes when studying compilers, language parsers, virtual
machines and JavaScript.

%prep
%setup -q -n %{name}-master
sed -i 's|/usr/local|/usr|' projects/ejscript-linux-default.mk

%build
#configure
#make_build
make -f projects/ejscript-linux-default.mk

%install
#make ME_ROOT_PREFIX=%{buildroot} -f projects/ejscript-linux-default.mk install
install -d %{buildroot}%{_bindir}
install -m755 build/linux-x64-default/bin/{ejs,ejsc,ejsman,ejsmod,ejsrun,mvc,utest} %{buildroot}%{_bindir}
install -d %{buildroot}%{_includedir}/ejs
install -m644 build/linux-x64-default/inc/* %{buildroot}%{_includedir}/ejs
install -d %{buildroot}%{_mandir}/man1
install -m644 doc/dist/man/* %{buildroot}%{_mandir}/man1

%files 
%doc *.md
%{_bindir}/*
%{_includedir}/ejs
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.7
- Rebuilt for Fedora
