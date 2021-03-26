%global debug_package %{nil}

Name:           viu
Version:        0.2.2
Release:        1
Summary:        A command-line application to view images from the terminal written in Rust
Group:          Terminals
License:        MIT
URL:            https://github.com/atanunq/viu
Source0:        https://github.com/atanunq/viu/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cargo

%description
Viu uses lower half blocks (▄ or \u2584) to fit 2 pixels into a single cell
by adjusting foreground and background colours accordingly. Features:
* Animated GIF support
* Accept media through stdin
* Custom dimensions

%prep
%autosetup

%build
cargo build --release --verbose
#cargo doc --verbose

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE-MIT
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed Oct 16 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuild for Fedora
