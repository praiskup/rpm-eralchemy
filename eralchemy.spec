# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/


%global sum()   Entity Relation Diagrams generation tool
%global desc \
ERAlchemy generates Entity Relation (ER) diagram (like the one below) from \
databases or from SQLAlchemy models.

Name:           eralchemy
Version:        1.2.10
Release:        0%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://github.com/Alexis-benoist/eralchemy
Source0:        https://github.com/Alexis-benoist/%name/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
ERAlchemy generates Entity Relation (ER) diagram from databases or from
SQLAlchemy models.


%package -n python3-%name
Summary:        %{sum}

%description -n python3-%name
%{desc}


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install



%files -n python3-%name
%license LICENSE.md
%python3_sitelib/*
%_bindir/eralchemy


%changelog
* Mon Sep 09 2019 Pavel Raiskup <praiskup@redhat.com> - 1.2.10-0
- initial RPM packaging
