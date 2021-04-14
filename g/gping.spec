%undefine _debugsource_packages

Name: gping
Version: 1.2.0
Release: 1
Summary: Ping, but with a graph
License: MIT
URL: https://github.com/orf/gping
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: cargo >= 1.42
BuildRequires: rust >= 1.42

%description
%{summary}.

%prep
%autosetup -p1

%install
export CARGO_PROFILE_RELEASE_BUILD_OVERRIDE_OPT_LEVEL=3
echo 'codegen-units = 1' >> Cargo.toml
cargo install --root=%{buildroot}%{_prefix} --path=.
rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json

%files
%license LICENSE
%doc readme.md
%{_bindir}/%{name}

%changelog
* Mon Jan 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
* Sun Dec  6 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.0-1
- build(update): 1.2.0
* Wed Dec  2 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- build(update): 1.1.0
* Sun Nov 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-1
- build(update): 1.0.1
* Thu Nov 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.7-1
- Initial package
