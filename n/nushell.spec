%undefine _debugsource_packages

Summary: A new type of shell
Name: nushell
Version: 0.81.0
Release: 1
License: MIT
Group: Development/Shell
URL: https://www.nushell.sh/
Source0: https://github.com/nushell/nushell/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: openssl-devel

%description
Nushell (or Nu for short) is a new shell that takes a modern, structured
approach to the commandline.

%prep
%setup -q

%build
cargo build

%install
cargo install --root=%{buildroot}%{_prefix} --path=.

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_bindir}/nu
%exclude /usr/.crates*
   
%changelog
* Sun Jun 11 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.81.0
- Rebuilt for Fedora
