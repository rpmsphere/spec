%undefine _debugsource_packages

Summary: The Agena Programming Language
Name: agena
Version: 2.30.4
Release: 1
License: MIT
Group: Development/Language
URL: http://agena.sourceforge.net/
Source0: http://downloads.sourceforge.net/agena/%{name}-%{version}-src.tar.gz

%description
Agena is an easy-to-learn procedural programming language designed to be used
in scientific, educational, linguistic, graphical, network, and many other
applications, including scripting.

Its syntax resembles very simplified Algol 68 with elements taken from Lua
and SQL.

Agena provides fast real and complex arithmetics, efficient text processing,
flexible data structures, intelligent procedures and package management, plus
various configuration facilities.

%prep
%setup -q -n %{name}-%{version}-src
sed -i 's|-DLUA_USE_LINUX|-DLUA_USE_LINUX -DLUA_RASPI_STRETCH -fPIC|' src/makefile
sed -i 's|/usr/agena/lib|/usr/share/agena/lib|' src/agnxlib.c
sed -i -e 's|/usr/lib|%{_libdir}|' -e 's|/include|/include/agena|' installers/rpmsuse/%{name}.pc

%build
#bash makealllinux.sh
cd src
make config linux

%install
cd src
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_libdir}
install -m755 libagena.* %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}/%{name}
install -m644 ag*.h cephes.h sofa.h sdncal.h interp.h moon.h sunriset.h prepdefs.h %{buildroot}%{_includedir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
mkdir %{buildroot}%{_datadir}/%{name}/{lib,doc,icons,schemes,scripting}
install -m644 ../lib/*.agn %{buildroot}%{_datadir}/%{name}/lib
install -m644 ../doc/agena.pdf ../doc/agena-crashcourse.pdf ../doc/agena.xls %{buildroot}%{_datadir}/%{name}/doc
install -m644 ../share/icons/*.gif ../share/icons/*.png ../share/icons/*.ico %{buildroot}%{_datadir}/%{name}/icons
install -m644 ../share/schemes/* %{buildroot}%{_datadir}/%{name}/schemes
install -m644 ../share/scripting/* %{buildroot}%{_datadir}/%{name}/scripting
install -Dm644 ../installers/rpmsuse/%{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc licence change.log lib/agenaini.spl
%{_bindir}/%{name}
%{_libdir}/lib%{name}.*
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.30.4
- Rebuilt for Fedora
