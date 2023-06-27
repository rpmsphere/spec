%undefine _debugsource_packages

Summary: Simple, extendable and embeddable scripting language
Name: duckscript
Version: 0.8.19
Release: 1
License: Apache 2.0
Group: Development/Languages
Source0: https://github.com/sagiegurari/duckscript/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/sagiegurari/duckscript
BuildRequires: cargo

%description
The language itself has only few rules and most common language features are
implemented as commands rather than part of the language itself.

%prep
%setup -q

%build
cargo build --release

%install
#cargo install --root=%{buildroot}%{_prefix} --path=.
install -d %{buildroot}%{_bindir}
install -m755 target/release/duck %{buildroot}%{_bindir}

%files 
%doc LICENSE *.md
%{_bindir}/duck

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.19
- Rebuilt for Fedora
