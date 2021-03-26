%global pkg_name trifecta

Name:           ghc-%{pkg_name}
Version:        1.6.2.1
Release:        1
Summary:        A modern parser combinator library with convenient diagnostics
License:        BSD-3-Clause
Group:          Development/Languages/Other
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-charset-devel
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-fingertree-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsers-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-reducers-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-utf8-string-devel

%description
A modern parser combinator library with slicing and Clang-style colored
diagnostics.

%package devel
Summary:        Haskell %{pkg_name} library development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%doc LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.markdown README.markdown examples

%changelog
* Mon Sep 11 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.2.1
- Rebuild for Fedora
* Sun Feb  5 2017 psimons@suse.com
- Update to version 1.6.2.1 with cabal2obs.
* Tue Nov 29 2016 psimons@suse.com
- Update to version 1.6.1 with cabal2obs.
* Thu Sep 15 2016 psimons@suse.com
- Update to version 1.6 revision 0 with cabal2obs.
* Sun Jul 10 2016 psimons@suse.com
- Update to version 1.5.2 revision 0 with cabal2obs.
