%undefine _debugsource_packages

Name: dmd
Version: 2.093.1
Release: 1
Summary: The D Programming Language reference compiler
Group: Development/Language
License: GPL
URL: http://dlang.org/
Source0: https://codeload.github.com/dlang/dmd/tar.gz/v%{version}#/%{name}-%{version}.tar.gz
Source1: https://github.com/dlang/phobos/archive/v%{version}.tar.gz#/phobos-%{version}.tar.gz
Source2: https://github.com/dlang/druntime/archive/v%{version}.tar.gz#/druntime-%{version}.tar.gz
Source4: %{name}.conf
BuildRequires: gcc-c++
BuildRequires: dmd
BuildRequires: curl-devel

%description
The D programming language is an object-oriented, imperative, multi-paradigm 
system programming language created by Walter Bright of Digital Mars. It 
originated as a re-engineering of C++, but even though it is mainly influenced 
by that language, it is not a variant of C++. D has redesigned some C++ features 
and has been influenced by concepts used in other programming languages, such as 
Java, Python, Ruby, C#, and Eiffel.

%prep
%setup -q -b 1 -b 2
#sed -i 's|-Wno-deprecated|-Wno-deprecated -Wno-narrowing|' src/posix.mak
#sed -i 's|bits/mathdef.h|complex.h|' src/root/port.c
#sed -i '/nan\.h/d' src/root/port.c
cd ..
ln -sf dmd-%{version} dmd
ln -sf phobos-%{version} phobos
ln -sf druntime-%{version} druntime

%build
cd ..
make -C dmd -f posix.mak MODEL=64
make -C druntime -f posix.mak MODEL=64
make -C phobos -f posix.mak MODEL=64

%install
#pushd ..
#make -C dmd -f posix.mak MODEL=64 install
#make -C druntime -f posix.mak MODEL=64 install
#make -C phobos -f posix.mak MODEL=64 install
#popd

mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_mandir}
cp -r docs/man/* %{buildroot}%{_mandir}

#cd ../install
install -Dm755 generated/linux/release/64/dmd %{buildroot}%{_bindir}/%{name}
cp -d ../install/linux/lib64/* %{buildroot}%{_libdir}
cp -r samples %{buildroot}%{_datadir}/%{name}
cp -r src %{buildroot}%{_includedir}/%{name}
cp -r ../install/src/* %{buildroot}%{_includedir}/%{name}
install -Dm644 %{SOURCE4} %{buildroot}%{_sysconfdir}/dmd.conf
install docs/man/man1/* %{buildroot}%{_mandir}/man1
install docs/man/man5/* %{buildroot}%{_mandir}/man5

%files
%doc README.md ../install/*.txt
%{_bindir}/*
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_sysconfdir}/*
%{_mandir}/man?/*
%{_libdir}/libphobos2.*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.093.1
- Rebuilt for Fedora
* Fri Aug 16 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.063.2-alt1
- new version
* Sat Feb 02 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.061-alt2
- Rebuild with -fPIC
* Sat Jan 19 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.061-alt1
- New version (Closes: #28302)
- Fix includes (Closes: #28394)
* Sat Dec 22 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt5
- Added provides
- Phobos in dmd
* Wed Oct 31 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt4
- Added Url in spec
- Added missed headers
- Fix dmd.config
* Tue Oct 16 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt3
- Excluded catdoc(conflicts with the package catdoc-0.94.2-alt4)
* Sun Oct 07 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt2
- Fix dmd.conf
* Tue Sep 25 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt1
- Initial build
