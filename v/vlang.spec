%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build
%global weekly 2022.39

Summary: The V Programming Language
Name: vlang
Version: 0.3.%{weekly}
Release: 1
License: MIT
Group: Development/Language
URL: https://github.com/vlang/v
Source0: https://github.com/vlang/v/archive/refs/tags/weekly.%{weekly}.tar.gz#/v-weekly.%{weekly}.tar.gz
BuildRequires: git make gcc

%description
Simple, fast, safe, compiled language for developing maintainable software.
Compiles itself in <1s with zero library dependencies.

%prep
%setup -q -n v-weekly.%{weekly}
#sed -i 's|byte{}|u8{}|' vlib/builtin/builtin_nix.c.v vlib/builtin/int.v vlib/strings/builder.c.v vlib/strconv/format_mem.c.v vlib/strconv/utilities.c.v vlib/os/os.c.v vlib/os/os_nix.c.v vlib/v/util/version/version.v
#sed -i '/type u8 = byte/d' vlib/builtin/int.v

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
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2022.39
- Rebuilt for Fedora
