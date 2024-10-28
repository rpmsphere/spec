%undefine _debugsource_packages
%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           libflux
Version:        0.195.2
Release:        2
Summary:        Influx data language
License:        Apache-2.0 AND MIT AND (Apache-2.0 OR MIT) AND Apache-2.0 WITH LLVM-exception AND CC-BY-3.0 AND CC-BY-SA-4.0 AND (Apache-2.0 OR BSL-1.0) AND BSD-3-Clause AND MPL-2.0 AND Zlib AND X11 AND Unicode-DFS-2016 AND Unicode-TOU
URL:            https://github.com/influxdata/flux
Source:         flux-%{version}.tar.xz
Source1:        vendor.tar.xz
Patch1:         disable-static-library.patch
Patch2:         fix-unsigned-char.patch
BuildRequires:  cargo
BuildRequires:  rust

%description
Flux is a lightweight scripting language for querying databases (like InfluxDB)
and working with data. It is part of InfluxDB 1.7 and 2.0, but can be run
independently of those. This repository contains the language definition and an
implementation of the language core.

%package devel
Summary:        Development libraries and header files for Influx data language
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the header files and libraries for building
programs using Influx data language.

%prep
%setup -q -n flux-%{version}
pushd libflux
tar -Jxf %{SOURCE1}

patch -p2 < %{PATCH1}
patch -p2 < %{PATCH2}
patch -p2 <<EOF
--- a/libflux/flux/build.rs
+++ b/libflux/flux/build.rs
@@ -79,5 +79,7 @@ fn main() -> Result<()> {
     let path = dir.join("stdlib.data");
     serialize(Environment::from(imports), fb::build_env, &path)?;

+    println!("cargo:rustc-cdylib-link-arg=-Wl,-soname,libflux.so.%{version}");
+
     Ok(())
 }
EOF
popd

%build
pushd libflux
RUSTFLAGS=%{rustflags} cargo build --release
RUSTFLAGS=%{rustflags} cargo build --features=doc --release --bin fluxdoc
popd

%install
install -D -m 644 libflux/include/influxdata/flux.h %{buildroot}%{_includedir}/influxdata/flux.h
install -D -m 755 libflux/target/release/libflux.so %{buildroot}%{_libdir}/libflux.so.%{version}
ln -sf ./libflux.so.%{version} %{buildroot}%{_libdir}/libflux.so

cat > flux.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name:           Flux
Version:        %{version}
Description: Library for the InfluxData Flux engine
Libs: -L%{_libdir} -lflux
Libs.private: -ldl -lpthread
Cflags: -I%{_includedir}
EOF

install -D -m 644 flux.pc %{buildroot}%{_libdir}/pkgconfig/flux.pc

install -D -m 755 libflux/target/release/fluxdoc %{buildroot}%{_bindir}/fluxdoc

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libflux.so.%{version}

%files devel
%license LICENSE
%doc README.md
%{_bindir}/fluxdoc
%{_libdir}/libflux.so
%{_libdir}/pkgconfig/flux.pc
%dir %{_includedir}/influxdata
%{_includedir}/influxdata/flux.h

%changelog
* Thu Sep 26 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.195.2
- Rebuilt for Fedora
* Sat Aug 17 2024 Matwey Kornilov <matwey.kornilov@gmail.com>
- Update to version 0.195.2, see:
  https://github.com/influxdata/flux/releases/
* Thu Jul  4 2024 Matwey Kornilov <matwey.kornilov@gmail.com>
- Switch back to InflxuData fork, since the Community fork is outdated.
- Add fix-unsigned-char.patch: fix build for aarch64
* Mon Nov 20 2023 Lubos Kocman <lubos.kocman@suse.com>
- Adjust license field based on legaldb scan
  * newly added Unicode-TOU compared to the previous scan
* Thu Oct 19 2023 Matwey Kornilov <matwey.kornilov@gmail.com>
- Use Rust 1.71 for build since build is known to be broken on 1.72+
* Fri Oct  6 2023 Matwey Kornilov <matwey.kornilov@gmail.com>
- Version 0.195.1:
  flux has been deprecated by InflxuData,
  switch the package to the Community fork
* Wed Mar 29 2023 Matwey Kornilov <matwey.kornilov@gmail.com>
- Update to version 0.193.0, see:
  https://github.com/influxdata/flux/releases/
- Drop 0001-fix-compile-error-with-Rust-1.64-5273.patch: upstreamed
- fluxc removed upstream
* Wed Oct 19 2022 Matwey Kornilov <matwey.kornilov@gmail.com>
- Add 0001-fix-compile-error-with-Rust-1.64-5273.patch:
    Fix build for rust1.64
* Tue Oct  4 2022 Matwey Kornilov <matwey.kornilov@gmail.com>
- Update to version 0.171.0, see:
  https://github.com/influxdata/flux/releases/
* Thu Jun 30 2022 Matwey Kornilov <matwey.kornilov@gmail.com>
- Add disable-static-library.patch: do not build static library
  (follow Factory guidelines).
* Thu Jun  9 2022 Matwey Kornilov <matwey.kornilov@gmail.com>
- Update to version 0.161.0, see:
  https://github.com/influxdata/flux/releases/
* Wed Dec  1 2021 Matwey Kornilov <matwey.kornilov@gmail.com>
- Fix libflux.so for Leap 15.2 and 15.3 (boo#1193120)
* Tue Nov 16 2021 Matwey Kornilov <matwey.kornilov@gmail.com>
- Update to version 0.139.0, see:
  https://github.com/influxdata/flux/releases/
- Build fluxc and fluxdoc binaries
* Tue Oct 26 2021 Matwey Kornilov <matwey.kornilov@gmail.com>
- Update to version 0.136.0, see:
  https://github.com/influxdata/flux/releases/
* Fri Sep 24 2021 Matwey Kornilov <matwey.kornilov@gmail.com>
- Update to version 0.131.0, see:
  https://github.com/influxdata/flux/releases/
* Thu Jun 10 2021 Michal Hrusecky <michal.hrusecky@opensuse.org>
- Update to version 0.117.3, see:
  https://github.com/influxdata/flux/releases/
* Wed May 19 2021 Michal Hrusecky <michal.hrusecky@opensuse.org>
- Update to version 0.116.0, see:
  https://github.com/influxdata/flux/releases/
* Fri Mar  5 2021 Matwey Kornilov <matwey.kornilov@gmail.com>
- Initial version
