%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build
%global weekly 2021.33.2

Summary: The V Programming Language
Name: vlang
Version: 0.2.2.%{weekly}
Release: 1
License: MIT
Group: Development/Language
URL: https://github.com/vlang/v
Source0: https://github.com/vlang/v/archive/refs/tags/weekly.%{weekly}.tar.gz

%description
Simple, fast, safe, compiled language for developing maintainable software.
Compiles itself in <1s with zero library dependencies.

%prep
%setup -q -n v-weekly.%{weekly}

%build
make

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}/vlang
cp -a v cmd vlib %{buildroot}%{_libexecdir}/vlang
ln -s ../libexec/vlang/v %{buildroot}%{_bindir}/v

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc doc/* LICENSE *.md
%{_bindir}/v
%{_libexecdir}/vlang

%changelog
* Sun Aug 22 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2git
- Rebuilt for Fedora
