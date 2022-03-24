Name: gvb
Summary: visual simulator of 1 and 2-dimensional vibrations
Version: 1.3
Release: 1
Group: science
License: Free Software
URL: http://www.pietrobattiston.it/gvb
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: python3-distutils-extra

%description
Good ViBrations (gvb) is a small program that aims at providing a nice
interface to play with waves in 1 or 2 dimensions.

It features several ways of setting initial conditions, as well as different
calculation methods and graphic outputs. It is also possible to dump animation
frames to png images in order to make a movie with them.

It relies on the Python library scipy to get the best possible performance in
calculations.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=/usr

%files
%doc ChangeLog COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/help/C/%{name}/
%{_datadir}/help/it/%{name}/
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/pixmaps/%{name}.svg
%{python3_sitelib}/gvb*

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
