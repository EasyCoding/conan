%global appname patch-ng

%global appsum Library to parse and apply unified diffs
%global appdesc Fork of the original python-patch library to parse \
and apply unified diffs

Name: python-%{appname}
Version: 1.17.2
Release: 1%{?dist}
Summary: %{appsum}

License: MIT
URL: https://github.com/conan-io/%{name}
Source0: %{pypi_source %{appname}}
BuildArch: noarch

BuildRequires: python3-devel

%description
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{appname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{appname}
%doc README.md
%{python3_sitelib}/patch_ng.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/patch_ng-*.egg-info

%changelog
* Wed Dec 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.17.2-1
- Initial SPEC release.