%global __spec_install_post %{nil}
%global debug_package %{nil}

Name: rust
Version: 1.9.0
Release: 9.1
Summary: A safe, concurrent, practical programming language
License: MIT or Apache-2.0
Group: Development/Languages/Other
URL: http://www.rust-lang.org
Source0: https://static.rust-lang.org/dist/%{name}c-%{version}-src.tar.gz
Source1: rust-stage0-2016-03-18-235d774-linux-i386-0e0e4448b80d0a12b75485795244bb3857a0a7ef.tar.bz2
Source2: rust-stage0-2016-03-18-235d774-linux-x86_64-1273b6b6aed421c9e40c59f366d0df6092ec0397.tar.bz2
BuildRequires: gcc-c++
BuildRequires: python
BuildRequires: perl
BuildRequires: chrpath
#AutoReqProv: off

%description
Rust is a curly-brace, block-structured expression language. It visually
resembles the C language family, but differs significantly in syntactic
and semantic details. Its design is oriented toward concerns of "programming
in the large", that is, of creating and maintaining boundaries -
both abstract and operational - that preserve large-system integrity,
availability and concurrency.

It supports a mixture of imperative procedural, concurrent actor,
object-oriented and pure functional styles. Rust also supports generic
programming and metaprogramming, in both static and dynamic styles.

%prep
%setup -q -n %{name}c-%{version}
mkdir dl
%ifarch x86_64
cp %{SOURCE2} dl
%else
cp %{SOURCE1} dl
%endif

%build
./configure --prefix=/usr
make

%install
%make_install

# Remove rpath.
#{ find $RPM_BUILD_ROOT%{_bindir} -type f ;
#    find $RPM_BUILD_ROOT -type f -name "*.so" ; } | xargs chrpath --delete

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/rust.conf <<EOF
%ifarch x86_64
%{_prefix}/lib/rustlib/x86_64-unknown-linux-gnu/lib
%else
%{_prefix}/lib/rustlib/i686-unknown-linux-gnu/lib
%endif
EOF

chmod +x $RPM_BUILD_ROOT%{_prefix}/lib/*.so
chmod -x $RPM_BUILD_ROOT%{_mandir}/*/rust*

cd %{buildroot}/usr/lib/rustlib
sed -i 's|%{buildroot}||g' manifest-rustc install.log manifest-rust-docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_datadir}/doc/rust
%{_bindir}/rust*
%config %{_sysconfdir}/ld.so.conf.d/rust.conf
%{_mandir}/*/rust*
%{_prefix}/lib/*.so
%{_prefix}/lib/rustlib

%changelog
* Thu Jun 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.0
- Rebuilt for Fedora
* Sun Apr 28 2013 Radek Miček
- Initial package
