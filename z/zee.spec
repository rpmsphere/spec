%undefine _debugsource_packages

Name:           zee
Version:        0.3.2
Release:        1
Summary:        A modern text editor for the terminal written in Rust
License:        Apache, MIT
URL:            https://github.com/zee-editor/zee
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cargo

%description
Zee is a modern editor for the terminal, in the spirit of Emacs.
It is written in Rust and it is somewhat experimental.

%prep
%autosetup
#sed -i 's|ropey = "1.4.1"|ropey = "1.5.0"|' zee/Cargo.toml zee-edit/Cargo.toml
sed -i 's|tree-sitter = "0.20.6"|tree-sitter = "0.20.10"|' */Cargo.toml

%build
cargo build --release --offline

%install
install -Dm755 target/release/zee %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE*
%doc *.md
%{_bindir}/%{name}

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora
