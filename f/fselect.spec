Summary:       fselect - Find files with SQL-like queries
Name:          fselect
Version:       0.8.1
Release:       1
License:       MIT
Group:         Development/Languages/Other
URL:           https://github.com/jhspetersson/fselect
Source0:       https://github.com/jhspetersson/fselect/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: cargo
BuildRequires: openssl-devel

%description
Find files with SQL-like queries

%prep
%setup -q
#sed -i -e 's|BUILDROOT_GOES_HERE|%{_builddir}/%{name}|g' %{_builddir}/%{name}/.cargo/config
sed -i 's|mp4parse = "0.12"|mp4parse = "0.12.1"|' Cargo.toml

%build
cargo build --release

%install
#cargo install --root=%{buildroot}%{_prefix}
#rm -f %{buildroot}%{_prefix}/.crates.toml
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 docs/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files 
%doc docs/usage.md LICENSE-APACHE LICENSE-MIT README.md
%{_bindir}/fselect
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.1
- Rebuilt for Fedora
* Wed Feb 1 2017 Petr Belyaev <upcfrost@gmail.com> - 2.75-1
- Initial Build
