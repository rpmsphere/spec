%global srcname face_recognition_models

Name:           python3-%{srcname}
Version:        0.3.0
Release:        3.1
Summary:        Trained models for the face_recognition python library
License:        CC0-1.0
URL:            https://github.com/ageitgey/face_recognition_models
Source0:        https://github.com/ageitgey/face_recognition_models/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildRequires:  python3-devel
#Requires:       python3-%{srcname}
BuildArch:      noarch

%description
This package contains only the models used by face_recognition.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc README.rst LICENSE
%{python3_sitelib}/*

%changelog
* Wed Aug 01 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuilt for Fedora
