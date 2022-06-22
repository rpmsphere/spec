%undefine _debugsource_packages

Summary: A secure JavaScript and TypeScript runtime
Name: deno
Version: 1.22.2
Release: 1
License: MIT
Group: Development/Language
URL: https://github.com/denoland/deno
Source0: https://codeload.github.com/denoland/deno/tar.gz/refs/tags/v%{version}#/%{name}-%{version}.tar.gz
BuildRequires: rust

%description
Deno is a simple, modern and secure runtime for JavaScript and
TypeScript that uses V8 and is built in Rust.

%prep
%setup -q

%build
cargo build --release -j 1

%install
#cargo install --root=%{buildroot}/usr --path=.
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc *.md
%{_bindir}/%{name}

%changelog
* Sun Jun 5 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.22.2
- Rebuilt for Fedora
