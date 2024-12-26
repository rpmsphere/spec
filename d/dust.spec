%undefine _debugsource_packages

Name:           dust
Version:        1.1.1
Release:        1
Summary:        A more intuitive version of du in rust
Group:          Text tools
License:        ASL
URL:            https://github.com/bootandy/dust
Source0:        https://github.com/bootandy/dust/archive/%{name}-%{version}.tar.gz
Source2:        cargo.config
BuildRequires:  cargo

%description
du + rust = dust. Like du but more intuitive.

%prep
%autosetup

%build
cargo build --release

%install
%__mkdir_p %{buildroot}%{_bindir}
cp target/release/dust %{buildroot}%{_bindir}/

%files
%doc LICENSE README.md
%{_bindir}/dust

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuilt for Fedora
* Tue May 12 2020 guillomovitch <guillomovitch> 0.5.1-1.mga8
+ Revision: 1583381
- imported package dust

