%define	pkgname missing-functions

Summary:	Functions in MATLAB but not in Octave
Name:       octave-%{pkgname}
Version:	1.0.2
Release:    14.1
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
URL:		http://octave.sourceforge.net/missing-functions/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.0.0
BuildRequires:  fltk, gnuplot, java-1.8.0-openjdk-headless, lua
BuildRequires:  octave-devel >= 3.0.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildArch:	noarch
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
BuildRequires:  llvm-devel
BuildRequires:  atlas urw-fonts

%description
Find functions that are in MATLAB but not in Octave.

%prep
%setup -q -c %{pkgname}-%{version}
cp %{SOURCE0} .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %{SOURCE0} 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}

%changelog
* Thu Jul 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 1.0.2-5
+ Revision: 123f26e
- MassBuild#464: Increase release tag
