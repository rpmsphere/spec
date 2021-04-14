%global __spec_install_post %{nil}

Name:           fsharp
Version:        4.0.1.1
Release:        21.1
Summary:        F# compiler, core library and core tools
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            http://fsharp.github.io
Source:         https://github.com/%{name}/%{name}/archive/%{version}.tar.gz
Patch1:         use-internal-nunit.patch
BuildRequires:  automake
BuildRequires:  mono-devel > 3.0
BuildRequires:  mono-wcf
BuildRequires:  mono-winfx
BuildRequires:  nunit
BuildArch:      noarch

%description
F# is a mature, open source, functional-first programming language
which empowers users and organizations to tackle complex computing
problems with simple, maintainable and robust code. It is used in
a wide range of application areas and is available across multiple
platforms.

%prep
%setup -q
%patch1 -p1

%build
autoreconf -ifv
%configure --libexecdir=%{_prefix}/lib/
make

%install
%make_install
rm -rf ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/monodroid
rm -rf ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/monotouch
rm -rf ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild

#fix script-without-shebang warnings
#find %{buildroot}%{_prefix}/lib/mono -iname "*.Fsharp.Targets" -type f -print0 | xargs -0 chmod -v -x
#find %{buildroot}%{_prefix}/lib/mono -iname "Fsharp.*.xml" -type f -print0 | xargs -0 chmod -v -x

#fix brp-25-symlink failure
#while read line
#do
#  src=`readlink -f "$line"`
#  echo "replacing link $line with file $src"
#  rm "$line"
#  cp "$src" "$line"
#done <<< "$(find %{buildroot}%{_prefix}/lib/mono/Reference* -type l)"

%files
%{_bindir}/fsharp*
%{_prefix}/lib/mono/4.5/*
%{_prefix}/lib/mono/gac/FSharp.*
%{_prefix}/lib/mono/gac/policy.*.FSharp.Core
%{_prefix}/lib/mono/Microsoft*
%{_prefix}/lib/mono/Reference*

%changelog
* Tue Jan 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.1.1
- Rebuilt for Fedora
* Thu Dec 10 2015 idonmez@suse.com
- Update to version 4.0.1.1
  * No changelog upstream
* Tue Dec  1 2015 idonmez@suse.com
- Update to version 4.0.1.0
  * No changelog upstream
- Refresh use-internal-nunity.patch
* Mon Oct 12 2015 idonmez@suse.com
- Update to version 4.0.0.4
* Sat Sep  5 2015 fwdsbs.to.11df@xoxy.net
- Build fixes:
  * added use-internal-nunit.patch: use nunit from project repo instead of external nuget package
  * fix brp-25-symlink failure by using hardlinks
  * fix other packaging problems
* Fri Sep  4 2015 idonmez@suse.com
- Update to version 4.0.0.3
* Tue May  5 2015 fwdsbs.to.11df@xoxy.net
- Minor fixes in spec file
* Tue May  5 2015 idonmez@suse.com
- Update to version 3.1.1.32
- Add mono-wcf dependency to fix compilation with Mono 4.0
- Remove _service file, not needed.
  Sat May  3 11:12:00 UTC 2014 - MihailJP
- Updated to version 3.1.1.11
