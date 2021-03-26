Name: python-pysmb
Summary: An experimental SMB/CIFS library written in pure Python
Version: 1.1.16
Release: 3.1
Group: Development/Libraries
License: GPL
URL: http://miketeo.net/wp/index.php/projects/pysmb
Source0: http://miketeo.net/files/Projects/pysmb/pysmb-%{version}.zip
BuildRequires: python-devel
BuildArch: noarch

%description
pysmb implements the client-side SMB/CIFS protocol (SMB1 and SMB2) which
allows your Python application to access and transfer files to/from SMB/CIFS
shared folders like your Windows file sharing and Samba folders.

%prep
%setup -q -n pysmb-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc CHANGELOG LICENSE README.txt
%{python_sitelib}/*

%changelog
* Fri Jul 24 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.16
- Rebuild for Fedora
