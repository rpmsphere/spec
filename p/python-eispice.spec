BuildRequires: gcc-gfortran python-devel tk-devel tcl-devel numpy atlas-devel
Summary:  Python SPICE simulator
Name:     python-eispice
Version:  0.11.6
Release:  7.1
License:  Other (See Source)
Group:    Science
Source:   eispice-0.11.6.tar.bz2
URL:      http://www.thedigitalmachine.net/eispice.html
Vendor:   thedigitalmachine
Patch:    eispice-0.11.6.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
eispice is a clone of the Berkley SPICE 3 Simulation Engine. It was originally
targeted toward PCB level Signal Integrity Simulation; simulating IBIS model
defined devices, transmission lines, and passive termination but the scope of
the tool has been slowly expanding to include more general purpose circuit
simulation features.

%prep
%setup -n eispice-0.11.6
%patch -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install \
            --root="$RPM_BUILD_ROOT" \
            --prefix="%{_prefix}"

%files
%defattr(-,root,root)
%{python_sitearch}/eispice.pth
%dir %{python_sitearch}/eispice
%{python_sitearch}/eispice/*

%post
ldconfig

%postun
ldconfig

%changelog
* Wed Dec 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.6
- Rebuilt for Fedora
