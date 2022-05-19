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

%build
cargo build --release --locked --offline

%install
install -Dm755 target/release/zee %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE*
%doc *.md
%{_bindir}/%{name}

%changelog
* Sun May 8 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora
