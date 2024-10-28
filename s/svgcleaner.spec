Name:           svgcleaner
Version:        0.9.5
Release:        1
Summary:        A software to remove unnecessary data from SVG files
License:        GPL-2.0-only
Group:          Productivity/Graphics/Other
URL:            https://github.com/RazrFalcon/svgcleaner
Source0:        v%{version}.tar.gz
Source1:        gui-v%{version}.tar.gz
Source2:        %name.vendor.tar.xz
Patch0:         svgcleaner-gui-suse.patch
BuildRequires:  cargo
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  hicolor-icon-theme
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  rust
Requires:       p7zip

%description
Svgcleaner reduces the size of an SVG image by removing useless data such as
- temporary data used by the vector editing application
- non-optimal SVG structure representation
- unused and invisible graphical elements

%package -n svgcleaner-gui
Summary:        Graphical user interface to svgcleaner
Group:          Productivity/Graphics/Other
Requires:       %{name} = %{version}
Requires:       p7zip

%description -n svgcleaner-gui
This package provides a Qt graphical user interface to svgcleaner.

%prep
%setup -q
%setup -q -a 1
%patch 0 -p1
%setup -q -D -T -a 2
mkdir cargo-home
cat >cargo-home/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
export CARGO_HOME=`pwd`/cargo-home/
cargo build --release %{?_smp_mflags}
cd svgcleaner-gui-%{version}
%qmake_qt5
%make_build

%install
mkdir build
export CARGO_HOME=`pwd`/cargo-home/
cargo install --root=build
mkdir -p %{buildroot}%{_bindir}
install -Dm0775 build/bin/svgcleaner %{buildroot}%{_bindir}/svgcleaner
cd svgcleaner-gui-%{version}
%make_install INSTALL_ROOT=%{buildroot}

%files
%license LICENSE.txt
%doc CHANGELOG.md FAQ.md data/help.txt
%{_bindir}/svgcleaner

%files -n svgcleaner-gui
%{_bindir}/%{name}-gui
%{_datadir}/applications/svgcleaner.desktop
%{_datadir}/icons/hicolor/scalable/apps/svgcleaner.svg

%changelog
* Wed Jan 15 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.5
- Rebuilt for Fedora
* Wed Feb  6 2019 sogal@opensuse.org
- Removed svgcleaner-gui dependency to p7zip-full as nothing provides it in
  openSUSE and the needed 7za component is already provided by p7zip
  (revert https://build.opensuse.org/request/show/616716)
* Wed Oct 10 2018 sogal@opensuse.org
- update to v0.9.5
  * removal of the transform attribute with a default value
  * a default Transform will be printed as matrix(1 0 0 1 0)
    and not as an empty string
  * attributes resolving during the defs regrouping
  * text with xml:space preprocessing
- update vendored sources
- refreshed svgcleaner-gui-suse.patch
* Wed Jun 13 2018 w01dnick@gmail.com
- svgcleaner-gui dependency changed to p7zip-full (7za is needed)
* Thu Apr 19 2018 jengelh@inai.de
- Repair bullet points characters in description. Simplify summary.
* Wed Apr  4 2018 mpluskal@suse.com
- Cleanup spec file with spec-cleaner
* Fri Mar 30 2018 sogal@volted.net
- Upgrade to 0.9.4
  * Crash during defs processing.
  * Crash during use resolving.
  * The --resolve-use option does not resolve used use now.
- Add svgcleaner-gui-suse.patch
* Tue Mar 27 2018 sogal@volted.net
- Upgrade to 0.9.3, major changes since 0.6.2:
  * Rewritten from C++ to Rust (3x faster)
  * Implemented own SVG parser and SVG DOM
  * GUI is in separated source now
  * Added a documentation for all cleaning options
  * Addition of many CLI options
  * Lots of fixes (see project page for details)
  * Main package is now svgcleaner
  * GUI is in svgcleaner-gui
* Mon Mar 10 2014 dmitry_r@opensuse.org
- Split package into svgcleaner and svgcleaner-cli
* Sun Mar  9 2014 dmitry_r@opensuse.org
- Update to version 0.6.2
  * ~3 times faster and ~10%% better cleaning.
  * Added replacing of equal elements with 'use'.
  * Added removing of elements out of viewbox.
  * Added transformation matrices applying.
  * Added trimming of 'id' attribute.
  * Added removing of equal 'filter' and 'clipPath' in 'defs'.
  * Added removing of Sketch namespaced elements and attributes.
  * Improved paths processing.
  * Improved removing of equal gradients.
  * Improved grouping of elements with similar attributes.
  * Improved transform matrices processing.
  * Improved ungrouping of containers.
  * Improved merging of gradients.
  * Improved rounding of numbers.
  * Improved removing of invisible elements.
  * New keys for CLI.
  * CLI now depends only on QtCore.
  * Moved from QtXml to TinyXML2.
  * Added saving of last cleaning options to GUI.
  * Added file tree to GUI.
  * Removed preset files.
  * A lot of fixes and speed optimizations.
* Fri Jan 11 2013 dmitry_r@opensuse.org
- Initial package, version 0.5
