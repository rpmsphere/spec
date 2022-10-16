#undefine _debugsource_packages

Summary: Alusus Programming Language
Name: alusus
Version: 0.9.0
Release: 1
License: Alusus Public License 1.0
Group: Development/Languages
Source0: https://github.com/Alusus/Alusus/archive/refs/tags/v%{version}.tar.gz#/Alusus-%{version}.tar.gz
URL: https://alusus.org/

%description
Alusus is designed to be a language for everything by making language features
hot-pluggable, and on a per-project basis (rather than per-environment).

%prep
%setup -q -n Alusus-%{version}
sed -i 's|lib/cmake/llvm|%{_lib}/cmake/llvm|' Sources/CMakeLists.txt

%build
cd Sources
%cmake -DLLVM_PATH=/usr
%cmake_build

%install
cd Sources
%cmake_install
#install -d %{buildroot}%{_bindir}
#install -m755 *-linux-build/%{name}* *-linux-build/stategraph %{buildroot}%{_bindir}
#install -d %{buildroot}%{_includedir}/%{name}
#install -m644 include/* %{buildroot}%{_includedir}/%{name}

%files 
%doc license.* *.md
#{_bindir}/*
#{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 02 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuilt for Fedora
