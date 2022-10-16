%undefine _debugsource_packages

Summary: A simple, expressive, embeddable programming language
Name: koto
Version: 0.11.0
Release: 1
License: MIT
Group: Development/Languages
#Source0: https://github.com/koto-lang/koto/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0: koto-main.zip
URL: https://koto.dev/
BuildRequires: cargo

%description
Koto is an embeddable scripting language, written in Rust. It has been designed
for ease of use and built for speed, with the goal of it being an ideal choice
for adding scripting to Rust applications.

%prep
%setup -q -n %{name}-main

%build
cargo build --release

%install
#cargo install koto_cli --root=%{buildroot}%{_prefix} --path=.
install -d %{buildroot}%{_bindir}
install -m755 target/release/koto %{buildroot}%{_bindir}

%files 
%doc LICENSE *.md
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.0
- Rebuilt for Fedora
