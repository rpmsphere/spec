%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build
%global weekly 2022.40

Summary: The V Programming Language
Name: vlang
Version: 0.4.3
Release: 1
License: MIT
Group: Development/Language
URL: https://github.com/vlang/v
#Source0: https://github.com/vlang/v/archive/refs/tags/weekly.%{weekly}.tar.gz#/v-weekly.%{weekly}.tar.gz
Source0: v-%{version}.tar.gz
BuildRequires: git make gcc

%description
Simple, fast, safe, compiled language for developing maintainable software.
Compiles itself in <1s with zero library dependencies.

%prep
#setup -q -n v-weekly.%{weekly}
%setup -q -n v-%{version}
#sed -i 's|byte{}|u8{}|' vlib/builtin/builtin_nix.c.v vlib/builtin/int.v vlib/strings/builder.c.v vlib/strconv/format_mem.c.v vlib/strconv/utilities.c.v vlib/os/os.c.v vlib/os/os_nix.c.v vlib/v/util/version/version.v
#sed -i '/type u8 = byte/d' vlib/builtin/int.v
sed -i 's|/usr/bin/env -S v|/usr/bin/v|' vlib/v/tests/script_with_no_extension
sed -i '36,37d' vlib/strconv/f32_str.c.v

%build
make

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}/%{name}
cp -a v v.mod cmd vlib thirdparty %{buildroot}%{_libexecdir}/%{name}
ln -s ../libexec/vlang/v %{buildroot}%{_bindir}/v

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc doc/* LICENSE *.md examples
%{_bindir}/v
%{_libexecdir}/%{name}

%changelog
* Sun Apr 07 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.3
- Rebuilt for Fedora
