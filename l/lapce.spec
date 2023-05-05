%undefine _debugsource_packages

Name:           lapce
Version:        0.2.4
Release:        1
Summary:        Lightning-fast and Powerful Code Editor written in Rust
License:        Apache-2.0
URL:            https://github.com/lapce/lapce
Source0:        https://github.com/lapce/lapce/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
install -Dm755 target/release/lapce-proxy %{buildroot}%{_bindir}/lapce-proxy
install -Dm755 extra/linux/dev.lapce.lapce.desktop %{buildroot}/usr/share/applications/dev.lapce.lapce.desktop
install -Dm766 extra/linux/dev.lapce.lapce.metainfo.xml %{buildroot}/usr/share/metainfo/dev.lapce.lapce.metainfo.xml
install -Dm766 extra/images/logo.png %{buildroot}/usr/share/pixmaps/dev.lapce.lapce.png

%files
%license LICENSE*
%doc *.md
%{_bindir}/%{name}
%{_bindir}/lapce-proxy
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/pixmaps/*.png

%changelog
* Sun Dec 11 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuilt for Fedora
