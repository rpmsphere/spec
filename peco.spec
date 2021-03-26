%undefine _missing_build_ids_terminate_build
%global gopath %{_datadir}/gocode

Summary:     Simplistic interactive filtering tool
Summary(ja): シンプルな対話式フィルタリングツール
Name:        peco
Version:     0.5.3git
Release:     1
License:     MIT License
Group:       Applications/Text
URL:         https://github.com/peco/peco
#Source:      https://github.com/peco/peco/archive/v%{version}.tar.gz#/peco-%{version}.tar.gz
Source:      %{name}-master.zip
BuildRequires: golang
#BuildRequires: golang(github.com/google/btree)
#BuildRequires: golang(github.com/mattn/go-runewidth)
#BuildRequires: golang(github.com/jessevdk/go-flags)
#BuildRequires: golang(github.com/nsf/termbox-go)
#BuildRequires: golang(github.com/pkg/errors)
#BuildRequires: golang(github.com/lestrrat/go-pdebug)

%description
peco is a simplistic interactive filtering tool
based on a python tool, percol, and written in Go.

%description -l ja
pecoはシンプルな対話式フィルタリングツールであり、
Python製のpercolをGo言語で実装したプログラムです。

%prep
%setup -q -n %{name}-master

%build
export BUILD_DIR=$(pwd)/.build
export GOPATH=${BUILD_DIR}:%{gopath}
make build
go build cmd/peco/peco.go

%install
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -m 755 peco ${RPM_BUILD_ROOT}%{_bindir}

%clean
%{__rm} -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE
%doc README.md Changes
%{_bindir}/%{name}

%changelog
* Mon Aug 12 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.3git
- Rebuild for Fedora
* Sat Jun 09 2018 Toshiaki Ara <ara_t@384.jp> 0.5.3-1
- update to 0.5.3
* Wed Jun 07 2017 IWAI, Masaharu <iwaim.sub@gmail.com> 0.5.1-1
- update to 0.5.1
- update BuildRequires
* Wed May 11 2016 Toshiaki Ara <ara_t@384.jp> 0.3.6-1
- update to 0.3.6
* Sun Apr 10 2016 Toshiaki Ara <ara_t@384.jp> 0.3.5-5
- correct SPEC file
* Fri Jan 29 2016 Toshiaki Ara <ara_t@384.jp> 0.3.5-4
- defile %%{gopath}
* Mon Jan 25 2016 IWAI, Masaharu <iwaim.sub@gmail.com> 0.3.5-3
- using golang-* RPM packages for BuildRequires
 - stop 'go get' in build section
- update build section
- add LICENSE, README.md and Changes
* Tue Jan 19 2016 Toshiaki Ara <ara_t@384.jp> 0.3.5-2
- build with Go
- change spec file
* Sun Jan 17 2016 Toshiaki Ara <ara_t@384.jp> 0.3.5-1
- new package
