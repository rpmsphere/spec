%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build
%global weekly 2021.38

Summary: The V Programming Language
Name: vlang
Version: 0.2.2.%{weekly}
Release: 1
License: MIT
Group: Development/Language
URL: https://github.com/vlang/v
Source0: https://github.com/vlang/v/archive/refs/tags/weekly.%{weekly}.tar.gz
BuildRequires: git

%description
Simple, fast, safe, compiled language for developing maintainable software.
Compiles itself in <1s with zero library dependencies.

%prep
%setup -q -n v-weekly.%{weekly}

%build
make

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}/%{name}
cp -a v cmd vlib %{buildroot}%{_libexecdir}/%{name}
ln -s ../libexec/vlang/v %{buildroot}%{_bindir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc doc/* LICENSE *.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%changelog
* Fri Sep 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2git
- Rebuilt for Fedora
