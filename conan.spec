%global appsum The open-source C/C++ package manager
%global appdesc A distributed, open source, package manager for C/C++

Name: conan
Version: 0.30.3
Release: 1%{?dist}
Summary: %{appsum}

License: MIT
URL: https://github.com/conan-io/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python3-devel

BuildRequires: python2dist(requests)
BuildRequires: python3dist(requests)
BuildRequires: python2dist(wheel)
BuildRequires: python3dist(wheel)
BuildRequires: python2dist(six)
BuildRequires: python3dist(six)

%description
%{appdesc}.

%package -n python2-%{name}
Summary: %{appsum}
Requires: python2dist(requests)
Requires: python2dist(six)
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
%{appdesc}.

%package -n python3-%{name}
Summary: %{appsum}
Requires: python3dist(requests)
Requires: python3dist(six)
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{appdesc}.

%prep
%autosetup -n %{name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{name}
%license LICENSE.md
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{name}
%license LICENSE.md
%doc README.rst
%{python3_sitelib}/*

%changelog

