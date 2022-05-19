#%undefine _debugsource_packages

Name:           lapce
Version:        0.0.12
Release:        1
Summary:        Lightning-fast and Powerful Code Editor written in Rust
License:        Apache-2.0
URL:            https://github.com/lapce/lapce
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cargo

%description
Lapce is written in pure Rust, with the UI in Druid. It uses Xi-Editor's Rope
Science for text editing, and the Wgpu Graphics API for rendering.

%prep
%autosetup

%build
cargo build --release

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE*
%doc *.md
%{_bindir}/%{name}

%changelog
* Sun May 8 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.12
- Rebuilt for Fedora
